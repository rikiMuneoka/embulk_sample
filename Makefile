.PHONY: embulk/*

# インストールと、実行権限の付与
embulk/setup:
	curl --create-dirs -o bin/embulk -L "http://dl.embulk.org/embulk-latest.jar"
	chmod +x bin/embulk
