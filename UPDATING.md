# Updating Airflow

This file aims to document the backwards-incompatible changes in Airflow and
assist people with migrating to a new version.

## 1.7 to 1.8

### DAGs now don't start automatically when created

To retain the old behavior, add this to your configuration:

```
dags_are_paused_at_creation = False
```

### Worker, Scheduler, Webserver, Kerberos, Flower now detach by default

The different daemons have been reworked to behave like traditional Unix daemons. This allows
you to set PID file locations, log file locations including stdin and stderr.

If you want to retain the old behavior specify ```-f``` or ```--foreground``` on the command line.