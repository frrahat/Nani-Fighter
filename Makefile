default:
	echo 'Nothing accomplished'

add-tag:
	git tag -a $(git_tag) -m "$(git_tag_message)"
	git push --tags

upload:
	python setup.py sdist
	twine upload dist/*
