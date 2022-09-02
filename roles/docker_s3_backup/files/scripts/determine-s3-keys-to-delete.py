#!/usr/bin/python
import os


def main():
    s3_result = eval(os.getenv("S3_RESULTS"))
    num_backups_to_keep = int(os.getenv("NUM_BACKUPS_TO_KEEP"))

    items_to_delete = []
    for res in s3_result:
        s3_keys = res["s3_keys"]
        # fetch all of the backups before the desired number.
        # these are the ones we want to delete.
        items_to_delete.extend(s3_keys[0:-num_backups_to_keep])

    for item in items_to_delete:
        print(item)


if __name__ == "__main__":
    main()
