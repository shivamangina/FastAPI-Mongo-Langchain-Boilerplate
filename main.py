# import logging
from dotenv import load_dotenv
import uvicorn
import click
import os
from app.core.config import get_config


@click.command()
@click.option(
    "--env",
    type=click.Choice(["dev", "prod"], case_sensitive=False),
    default="dev",
)
@click.option(
    "--debug",
    type=click.BOOL,
    is_flag=True,
    default=False,
)
def main(env: str, debug: bool):

    # Load the .env file
    load_dotenv()
    os.environ["ENV"] = env
    os.environ["DEBUG"] = str(debug)

    # TODO: Configure logging
    # logging.basicConfig(level=logging.INFO)
    # logger = logging.getLogger(__name__)
    config = get_config()

    uvicorn.run(
        app="app.server:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True if config.ENV != "prod" else False,
        workers=1,
    )


if __name__ == "__main__":
    main()
