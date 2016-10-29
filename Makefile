AUTHORS:
	git shortlog --numbered --summary | awk -F'\t' '{ print $2 }' > AUTHORS
