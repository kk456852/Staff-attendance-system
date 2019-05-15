import os

from flask_migrate import Migrate

from app import create_app, db

app = create_app()

migrate = Migrate(app, db)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command()
def ipy():
    """Open IPython Debug Shell"""
    ctx = app.app_context()
    ctx.push()
    from app.model import (Department, Leave,
                           Overtime, OvertimeSituation, TemporaryOvertime, Report,
                           Punch, SignSheet, WorkSituation, User, WorkArrangement)
    __import__('IPython').embed()
    ctx.pop()


@app.cli.command()
def init_db():
    """Init database and create basic test data."""
    db.drop_all()
    db.create_all()
