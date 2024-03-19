# Skrypt do synchronizacji plików lokalnie -> ssh

## Skrypt prawdopodobnie nie działa na windowsie

1. Zainstaluj wymagane programy:

- python
- [watchman](https://facebook.github.io/watchman/docs/install)
  - macOS: `brew install watchman`
  - Ubuntu: [dokumentacja](https://facebook.github.io/watchman/docs/install#ubuntu-prebuilt-debs)
- rsync
  - `brew install rsync`

2. Zmodyfikuj `config.json`
3. Dodaj klucze do `~/.ssh` i chociaż raz połącz się z serwerem by dodać go do `authorized_keys`
4. Uruchom `python3 create_watchman_config.py`
