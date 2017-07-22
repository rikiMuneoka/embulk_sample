.PHONY: embulk/* preview run

# 環境変数のファイル
DOT_ENV_FILE_PATH = $(CURDIR)/.env

embulk=./bin/embulk

# インストールと、実行権限の付与
embulk/setup:
	curl --create-dirs -o bin/embulk -L "http://dl.embulk.org/embulk-latest.jar"
	chmod +x bin/embulk

preview:
	$(embulk) preview -b . user.yml.liquid

run:
	$(embulk) run -b . user.yml.liquid
