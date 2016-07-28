build_js:
	cd static && webpack --display-error-details

build_css:
	sass static/src/scss/base.scss static/css/base.css

startgunicorn:
	supervisorctl start evilka

reloadgunicorn:
	supervisorctl status evilka | sed "s/.*[pid ]\([0-9]\+\)\,.*/\1/" | xargs kill -HUP

restartgunicorn:
	supervisorctl restart evilka

stopgunicorn:
	supervisorctl stop evilka

clean_pyc:
	@find `pwd` \( -name '*.pyc' -o -name '*.ptlc' \) -type f -delete
