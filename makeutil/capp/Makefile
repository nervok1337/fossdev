.PHONY: another-app

#build не совпадает с именем выходного файла app, будет перекомпилировать и пересобирать
build: main.c
	gcc main.c -o app

#app совпадает с app будет сравнивать время изменений, не перекомпилировать если изменений нет
app: main.c
	gcc main.c -o app

#игнорирует отсутствие изменений и все равно выполняет из-за .PHONY (отключает зависимость файловой системы)
another-app: main.c
	gcc main.c -o another-app