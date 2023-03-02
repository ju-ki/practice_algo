url = "atcoder.jp/contest/"
contest = "abc"
id = "a"

get_question:
	mkdir ${id}
	mkdir ${id}/tests
	oj download  ${url} -d ${id}/tests
	touch ${id}/main.py

get_question_without_url:
	mkdir ${contest}_${id}
	mkdir ${contest}_${id}/tests
	oj download  https://atcoder.jp/contests/${contest}/tasks/${contest}_${id} -d ${contest}_${id}/tests
	touch ${contest}_${id}/main.py

run_test:
	oj test -c "python3 ./${id}/main.py" -d ${id}/tests/

run_test_without_url:
	oj test -c "python3 ./${contest}_${id}/main.py" -d ${contest}_${id}/tests/

submit:
	oj submit ${url} ./${id}/main.py

submit_without_url:
	oj submit https://atcoder.jp/contests/${contest}/tasks/${contest}_${id} ./${contest}_${id}/main.py

