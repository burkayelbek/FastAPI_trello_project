import uvicorn
from src.trello_case_basic import app
from argparse import ArgumentParser
from dotenv import load_dotenv
from src.base.database import get_db
from src.models.comment import CommentModel
from src.models.user import UserModel
from src.models.project import ProjectModel
from src.models.job import JobModel
from fastapi.responses import RedirectResponse
from src.base.settings import Settings

settings = Settings()


def create_tables():
    CommentModel.metadata.create_all(bind=settings.postgresql_database_connection())
    UserModel.metadata.create_all(bind=settings.postgresql_database_connection())
    ProjectModel.metadata.create_all(bind=settings.postgresql_database_connection())
    JobModel.metadata.create_all(bind=settings.postgresql_database_connection())


def parse_arguments() -> ArgumentParser:
    """
    This Function Get Argument and Parse
    :return: Argument Parser
    """
    # Create argument parser
    parser = ArgumentParser()

    # Positional mandatory arguments
    parser.add_argument("-d", "--debug", help="Is Debug Mode", type=bool,
                        default=False)
    parser.add_argument("-r", "--reload", help="Change Reload", type=bool,
                        default=False)
    parser.add_argument("-log", "--access-log", help="Access Log Open or Close",
                        type=bool, default=False)
    parser.add_argument("-env", help="Environment File Path", type=str,
                        default=".env")

    # Parse arguments
    args = parser.parse_args()

    return args


def run(args: ArgumentParser):
    """
    This function run Fast API with Uvicorn
    :param args:
    :return:
    """
    uvicorn.run(
        app="trello_case_basic.base_router:app",
        host="0.0.0.0",
        port=8000,
        reload=args.reload,
        debug=args.debug,
        access_log=args.access_log,
        env_file=args.env,
    )


if __name__ == "__main__":
    run(args=parse_arguments())
