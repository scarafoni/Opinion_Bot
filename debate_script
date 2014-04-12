#!/bin/bash
touch lib_text.txt
touch con_text.txt

cat personalities/bloomberg/MASTER.txt > lib_text.txt
cat personalities/limbaugh/MASTER.txt > con_text.txt
gram=3
i=1
while [ $i -le 1000 ]
do
	printf "RUSH_LIMBOT:\n "
	python src/Opinion_Bot.py con_text.txt $gram -o lib_text.txt
	printf "\n\n\n"
	printf "MICHAEL_BLOOMBOT:\n " 
	sleep 5
	python src/Opinion_Bot.py lib_text.txt $gram -o con_text.txt
	printf "\n\n\n"

	(( i++ ))
done

sleep 3
printf "Who wins? \n ... \n\n\n"
sleep 2
printf "Neither. Both don't make sense.\n\n"
sleep 1
printf "Moral: Stop listening to political pundits.\n"
sleep 1

rm lib_text.txt
rm con_text.txt
