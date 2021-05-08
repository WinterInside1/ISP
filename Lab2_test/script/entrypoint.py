import argparse
import logging
from CustomSerializer.task.basic_serializer_creator import basic_creator

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

arg = argparse.ArgumentParser(description="Serialized object conversion")

arg.add_argument(
    'file_source',
    type=str,
    help='Path to source file'
)

arg.add_argument(
    'ext_source',
    type=str,
    help='Type of information in source file'
)

arg.add_argument(
    'ext_target',
    type=str,
    help='Type of information in target file'
)

arg.add_argument(
    "--file_target",
    type=str,
    default=None,
    help="Target file name"
)


def convert(file_source, ext_source, ext_target, file_target):
    ext_source = ext_source.lower()
    ext_target = ext_target.lower()
    if ext_source == ext_target:
        logging.error("Same extensions. Not converted.")
        return
    try:
        parser_from = basic_creator(ext_source)
        obj = parser_from.load(file_source)
    except Exception as ex:
        logging.error(ex)
        return
    if obj is None:
        logging.error("Empty object")
        return
    if file_target is None:
        file_target = file_source + "." + ext_target
    try:
        parser_to = basic_creator(ext_target)
        parser_to.dump(obj, file_target)
    except Exception as ex:
        logging.error(ex)
        return


args = arg.parse_args()
logging.info(f"Converting {args.file_source} file")
logging.info(f"from {args.ext_source} to {args.ext_target}")
logging.info(f"Target file name is {args.file_target}")
convert(args.file_source, args.ext_source, args.ext_target, args.file_target)
logging.info("Ending of conversion.")
