# Minecraft Server Starter Kit

## Installation

#### Create Virtual Environment
```sh
python3 -m venv .venv
```
```sh
source .venv/bin/activate
```

#### Install Dependencies
```sh
pip install --editable .
```

## Usage

| Command List |
| :--- |
| create |
| start |
| stop |
| logs |
<!-- | shell | -->


### Create Server
```sh
mcli server create [-p,-v,-t,-m,-d,-vd]
```
Options
- --port
- --version
- --type
- --memory
- --difficulty
- --view-distance


### Start Server
```sh
mcli server start
```

### Stop Server
```sh
mcli server stop [--all]
```
Options
- --all

### Stop Server
```sh
mcli server logs
```