import models
import db
import os


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
