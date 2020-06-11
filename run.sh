pip3 install beautifulsoup4
pip3 install pytz
export all_proxy="https://<proxy>:<port>/"

echo "CircuitBuildTimeout 10">>/etc/tor/torrc
echo "LearnCircuitBuildTimeout 0">>/etc/tor/torrc
echo "MaxCircuitDirtiness 10">>/etc/tor/torrc

tor &
python3 parse.py