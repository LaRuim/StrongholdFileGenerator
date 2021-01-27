# Strongold Navigator

A project that will aim to find the optimal route through a Stronghold.

## Installation
These installation instructions are desgined for Linux systems; Windows instructions will be added at a later date.

### 0. Fork, Clone and Extract:
* Fork the repository, and in a terminal opened in a folder of your choosing, run:
```
    git clone [your_forked_repository_url]
```
* Extract the downloaded folder and navigate to inside the folder.
### 1. Python dependencies:

* Set up a virtual environment. Run ```sudo apt install python3-venv``` if you do not have venv in your system.

```
    python3 -m venv [yourVenv]
```

* Activate your virtual environment.
```
    source [yourVenv]/bin/activate
```
* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the Python3 requirements for the project, as shown:

```
    pip install -r requirements.txt
```

### 2. Java dependencies:

* Follow [this](https://opensource.com/article/19/11/install-java-linux) guide to install Java on your Linux system.

## Building

Fire up a terminal in the root folder of the project. To build the Generator, run:

```
    ./gradlew buildNeeded
    ./gradlew build
    ./gradlew jar
```

## Usage

Navigate to app. You should see a layout.jar file. To view the command-line-arguments, run:

```
    java -jar layout.jar -h
```

Now, in a terminal, run:

```
    java -jar layout.jar [OPTIONS] > sample_output.txt
```

Navigate back to the root directory of the project, where sample_output will have been created. Now run:

```
    python parser.py > parsed_layout.txt
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Status
Output can be parsed into a readable format.