# WTF COVID-19 Ohio

A [WTF](https://wtfutil.com/) (`wtfutil`) dashboard module for the COVID-19 data from the Ohio Department of Health

Data: https://coronavirus.ohio.gov/wps/portal/gov/covid-19/home

![](screenshot.png)

## Setup

Requires [WTF](https://github.com/wtfutil/wtf) and [Docker](https://www.docker.com/).

## Install

Add the module config to `wtf.mods` in your WTF config file:

```yaml
wtf:
  ...
  mods:
    ...
    covid-19-ohio:
      type: cmdrunner
      title: COVID-19 Ohio
      cmd: docker
      args: [ run, --rm, tedmiston/wtf-covid-19-ohio:latest ]
      position:
        top: 4
        left: 0
        height: 2
        width: 1
      refreshInterval: 1800  # 30 minutes
      enabled: true
```

The config file is located at `~/.config/wtf/config.yml` by default.

The module runs a Docker container so it should *just work*.

## Quickstart

Just run the WTF dashboard:

```shell
$ wtfutil
```
