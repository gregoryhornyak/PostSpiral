# PostSpiral

PostSpiral is a Letterloop clone, which aims to provide a **free**, **open-source** solution of a private group newsletters for friends.

## Principles

- Only English expressions in the source code
- Use snake case (some_thing) for own contribution
- Consider security, as any data on the server can be accessible from outside (due to HTTP protocol)
- Do not use Microsoft Windows in the development process (except as an SSH client)
- Use a testing branch for testing purposes, and the main branch for the stable release
- Aim for a solution, not a tool-kit (less modular, less options)

## Installation

### Prerequisites

- AWS account - *to host the server*
- Gmail account - *to send emails*
- Outlook account - *why not*
- Github account - *to host (forked) project repository*
- Linux distro (e.g. Ubuntu) - *to develop the app*
- Friends 🙃 - *self-explanatory*

### AWS setup

### Gmail setup

### Server setup

```bash
git clone <repo>
```

## Usage

```bash
export FLASK_APP=app.py && flask run;
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)


Server running properly
- responsive for updates
- auto-updates website
- temporary offline message available
- basic login implemented
- sample newsletter issue included

END