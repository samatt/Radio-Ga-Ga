import os,subprocess

presentation = 'week-3/img'
def convert(k,v):
	for i,input in enumerate(v):
		output = '../{}/{}-{}.JPG'.format(presentation,k,i)
		#using imagemagick
		print output
		convert = ['convert',os.path.join(k,input), '-resize','2048',output]
		print convert[-1]


img_dir = 'images-raw'
places = [f for f in os.listdir(img_dir) if os.path.isdir(img_dir+'/'+f) ]
print '{}/{}'.format(img_dir,places[0])
files = {p:os.listdir('{}/{}'.format(img_dir,p)) for p in places}

[convert(k,v)for k,v in(dict.iteritems(files))]