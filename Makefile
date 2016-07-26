run_webpack:
	cd static && webpack --display-error-details

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
