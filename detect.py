import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileModifiedHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File {event.src_path} has been modified.")

def main():
    watch_directory = os.path.join(os.getcwd(), "test_files")

    event_handler = FileModifiedHandler()
    observer = Observer()
    observer.schedule(event_handler, watch_directory, recursive=True)

    print(f"Monitoring directory: {watch_directory}")

    try:
        observer.start()
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        print("File monitoring stopped.")

if __name__ == "__main__":
    main()
