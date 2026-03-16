import os

def main():
    env = os.environ.get('VIRTUAL_ENV')

    if env:
        print(f'Your current virtual env is {env}')
    else:
        print('No virtual environment detectedв')

if __name__ == '__main__':
    main()