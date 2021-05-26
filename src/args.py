from argparse import ArgumentParser


class Arguments:
    def add_arguments(self) -> None:
        self.parser.add_argument(
            "--district",
            metavar="district",
            type=str,
            help="District ID"
        )
        self.parser.add_argument(
            "--pincode",
            metavar="pincode",
            type=str,
            help="Pincode",
        )

        self.parser.add_argument(
            "--telegram",
            metavar="telegram",
            required=True,
            type=str,
            help="Telegram username"
        )

        self.parser.add_argument(
            "--dose",
            metavar="dose",
            default=1,
            type=str,
            help="Dose Number"
        )

    def __init__(self) -> None:
        self.parser = ArgumentParser(
            description="Command Line Arguments for Pls Give Vaccine"
        )
        self.add_arguments()

    def get_arguments(self) -> None:
        args = self.parser.parse_args()
        if not args.district and not args.pincode:
            raise Exception("Invalid arguments.")
        return args.district, args.pincode, args.telegram, args.dose
