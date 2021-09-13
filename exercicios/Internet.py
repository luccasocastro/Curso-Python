import speedtest
s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()
s.results.share()
results_dict = s.results.dict()
print(results_dict)
