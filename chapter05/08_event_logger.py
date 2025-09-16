from datetime import datetime

def log_event(event_type: str, **kwargs: dict) -> None:

    print(f'Event type: {event_type}')

    timestamp = datetime.now().isoformat()
    print(f'Timestamp: {timestamp}')

    for k, v in kwargs.items():
        print(f'{k} : {v}')


def main():
    log_event('User Login', user='John Doe', status='success', ip='192.168.1.1')
    log_event('File Upload', user='John Doe', status='Failure', filename='report.pdf', reason='File too large')

if __name__ == '__main__':
    main()