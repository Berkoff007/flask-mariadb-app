import os
import logging
from app import app, db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Starting the application...')

    with app.app_context():
        db.create_all()
        logger.info('Database created successfully.')

    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
