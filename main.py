import json
import argparse
from purchases import generate_json, send_request, extract_purchase, insert_into_purchases


parser = argparse.ArgumentParser(
    prog='command.py',
    usage='get purchase from image via Google Cloud Vision API.',
    description='description',
    epilog='end',
    add_help=True,
)
parser.add_argument('-k', '--key',
                    help='API key for Google Cloud API.',
                    required=True,)
parser.add_argument('-i', '--image',
                    help='Image file path to be annotated.',
                    required=True,)


def main():
    args = parser.parse_args()

    generated = generate_json.GenerateJson()
    request_data = json.dumps(generated.generate(args.image))

    sent = send_request.SendRequest()
    response = sent.send(request_data, args.key)

    purchase_histories = extract_purchase.MakePurchaseHistory()
    purchased = purchase_histories.make_purchase_history(response)

    insert_into_purchases.InsertIntoPurchases(purchased)

    return purchased


if __name__ == '__main__':
    result = main()
    print(result)
