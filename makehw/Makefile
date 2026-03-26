.DEFAULT_GOAL := help

create-project:
ifndef PROJECT
	$(error must pass PROJECT)
endif
	mkdir -p $(PROJECT)
	cp ProjectMakefile $(PROJECT)/Makefile

remove-project:
ifndef PROJECT
	$(error must pass val via PROJECT)
endif
	rm -rf $(PROJECT)
