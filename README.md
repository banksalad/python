# Rainist Python Project Template

## Usage

```bash
$ cookiecutter https://github.com/rainist/python
```

### Options

```bash
project_name [Python Project]: My Python Project
```

프로젝트 이름을 설정할 수 있습니다. 보통의 이름을 적듯 `-` 와 `_` 없이 설정합니다.

```bash
project_slug [my-python-project]: sample-python
```

프로젝트 폴더 이름을 설정할 수 있습니다. 보통 GitHub Repository로 쓰이는 이름과 같게 설정합니다.

```bash
package_name [samplepython]: app
```

프로젝트 폴더 안에 파이썬 코드가 담길 패키지 폴더 이름을 설정할 수 있습니다. 이 패키지 이름을 기반으로 `pylint`, 커버리지 측정, `Dockerfile` 설정이 이루어집니다.

```bash
Select python_version:
1 - 3.7
2 - 3.6
Choose from 1, 2 [1]:
```

사용할 파이썬 런타임 버전을 설정할 수 있습니다. `Dockerfile`, `mypy` 에서 사용됩니다.

```bash
Select use_mypy:
1 - n
2 - easy mode
3 - hard mode
Choose from 1, 2, 3 [1]: 3
```

[`mypy`](https://github.com/python/mypy) 사용 여부를 설정할 수 있습니다. 설정 시 `pre-push` hook과 `make check` 과정에 `mypy` 가 추가됩니다.

* `easy mode`: 타입 힌팅이 있는 함수들만 가지고 타입 검사를 수행합니다.
* `hard mode`: 타입 힌팅이 없는 함수까지 경고를 발생시킵니다.

```bash
use_black [n]: y
```

[`black`](https://github.com/ambv/black) 사용 여부를 설정할 수 있습니다. 설정 시 `pre-push` hook과 `make check`, `make format` 과정에 `black` 이 추가됩니다.
