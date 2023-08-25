# Project: Configuration Management with Puppet

![Project Badge](https://img.shields.io/badge/Status-In%20Progress-yellow)

This project is part of a learning journey focusing on configuration management with Puppet. The goal is to gain a deeper understanding of automating infrastructure tasks and managing system configurations using Puppet.

## Table of Contents

- [Background](#background)
- [Resources](#resources)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Background

During my time at SlideShare, I was involved in developing an auto-remediation tool named Skynet. This tool monitored, scaled, and fixed cloud infrastructure using Puppet. One incident highlighted the power of configuration management: a bug in the code resulted in shutting down a significant portion of our conversion infrastructure. Thanks to Puppet, we were able to swiftly recover and restore normal operation.

Read the full story on [Twitter](https://twitter.com/devopsreact/status/836971570136375296).

## Resources

For a better understanding of configuration management and Puppet, consider going through the following resources:

- [Intro to Configuration Management](#)
- [Puppet Resource Type: File](#)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](#)
- [Puppet Lint](#)
- [Puppet Emacs Mode](#)

## Requirements

### General

- All files are interpreted on Ubuntu 20.04 LTS.
- Files end with a new line.
- A `README.md` file at the root is mandatory.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without errors.
- Puppet manifests must run without errors.
- Puppet manifests' first line must be a comment explaining the manifest's purpose.
- Puppet manifest files must end with the `.pp` extension.

## Getting Started

Follow these steps to set up the project on your local system:

1. Clone this repository to your local machine.
2. Ensure you have Ubuntu 20.04 LTS installed.
3. Install required packages using the commands provided in the [Background Context](#background) section.
4. Review and understand the Puppet manifests.
5. Apply Puppet manifests to configure your environment.

## Usage

Explain how to use the Puppet manifests and how they can be applied to achieve configuration management goals.

## Contributing

Contributions to this project are welcome! If you find issues or want to enhance the project, feel free to submit pull requests.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your fork.
4. Submit a pull request.

Please adhere to the code style and guidelines specified in the project.

## License

This project is licensed under the [MIT License](LICENSE).
