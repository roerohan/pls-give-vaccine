[![Issues][issues-shield]][issues-url]
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/roerohan/pls-give-vaccine">
    <img src="https://project-logo.png" alt="Logo" width="80">
  </a> -->

  <h3 align="center">Pls Give Vaccine</h3>

  <p align="center">
    A script to spam yourself with vaccine notifications.
    <br />
    <a href="https://github.com/roerohan/pls-give-vaccine"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/roerohan/pls-give-vaccine">View Demo</a>
    ·
    <a href="https://github.com/roerohan/pls-give-vaccine/issues">Report Bug</a>
    ·
    <a href="https://github.com/roerohan/pls-give-vaccine/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contributors](#contributors-)



<!-- ABOUT THE PROJECT -->
## About The Project

Spam yourself with messages and calls (potentially) upon availability of vaccines (in India).

### Built With

* [Python](https://www.python.org/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- python

### Installation
 
1. Clone the Repo
```sh
git clone https://github.com/roerohan/pls-give-vaccine.git
```


<!-- USAGE EXAMPLES -->
## Usage

To start the script, run the following command:

- Using district ID
```sh
python main.py --district <district-id> --telegram <telegram-username> --dose <dose-number>
```

- Using pincode
```sh
python main.py --pincode <pincode> --telegram <telegram-username> --dose <dose-number>
```

To get a list of possible options, run `-h`.

```sh
$ python3 main.py -h                                           


To receive calls, visit https://api2.callmebot.com/txt/login.php and authenticate using telegram.


usage: main.py [-h] [--district district] [--pincode pincode] --telegram telegram [--dose dose]

Command Line Arguments for Pls Give Vaccine

optional arguments:
  -h, --help           show this help message and exit
  --district district  District ID
  --pincode pincode    Pincode
  --telegram telegram  Telegram username
  --dose dose          Dose Number
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/roerohan/pls-give-vaccine/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

You are requested to follow the contribution guidelines specified in [CONTRIBUTING.md](./CONTRIBUTING.md) while contributing to the project :smile:.

<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for more information.




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[roerohan-url]: https://roerohan.tech
[issues-shield]: https://img.shields.io/github/issues/roerohan/pls-give-vaccine.svg?style=flat-square
[issues-url]: https://github.com/roerohan/pls-give-vaccine/issues

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://sid200026.github.io/"><img src="https://avatars.githubusercontent.com/u/42297087?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Siddharth Singha Roy</b></sub></a><br /><a href="https://github.com/roerohan/pls-give-vaccine/commits?author=Sid200026" title="Documentation">📖</a> <a href="https://github.com/roerohan/pls-give-vaccine/commits?author=Sid200026" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/roerohan"><img src="https://avatars.githubusercontent.com/u/42958812?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rohan Mukherjee</b></sub></a><br /><a href="https://github.com/roerohan/pls-give-vaccine/commits?author=roerohan" title="Documentation">📖</a> <a href="https://github.com/roerohan/pls-give-vaccine/commits?author=roerohan" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!