import os
from database import init_db

if __name__ == '__main__':
  if not os.path.exists('db'):
    os.makedirs('db')
  init_db()


