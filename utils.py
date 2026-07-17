from pathlib import Path
import logging


def ensure_dir(path):

    Path(path).mkdir(
        parents=True,
        exist_ok=True
    )


def setup_logger(logfile):

    ensure_dir(Path(logfile).parent)

    logging.basicConfig(

        filename=logfile,

        level=logging.INFO,

        format="%(asctime)s %(levelname)s %(message)s"

    )

    return logging.getLogger("TVBox")


def backup_file(src, history_dir):

    src = Path(src)

    if not src.exists():
        return

    ensure_dir(history_dir)

    dst = Path(history_dir) / src.name

    dst.write_bytes(src.read_bytes())
