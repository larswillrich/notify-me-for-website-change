pip3 install --target ./package beautifulsoup4
pip3 install --target ./package pytz
pip3 install --target ./package requests
pip3 install --target ./package json
pip3 install --target ./package datetime

cd package
zip -r9 lambda_function_payload.zip .
zip -g lambda_function_payload.zip ../runInLambda.py
zip -g lambda_function_payload.zip ../sendMail.py
zip -g lambda_function_payload.zip ../config.json
zip -g lambda_function_payload.zip ../search.py
cd ..
terraform apply