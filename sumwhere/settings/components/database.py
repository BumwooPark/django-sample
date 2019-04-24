from sumwhere.settings import BASE_DIR, ENV


DATABASE_LIST = {
	'dev' : {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': 'sumwhere',
	        'USER': 'root',
	        'PASSWORD': '1q2w3e4r',
	        'HOST': '127.0.0.1',
	        'PORT': '3306',
	        'OPTION': {'charset':'utf8mb4'}
	    }
	},
	'prod': {
		'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': 'sumwhere',
	        'USER': 'root',
	        'PASSWORD': '1q2w3e4r',
	        'HOST': '127.0.0.1',
	        'PORT': '3306',
	        'OPTION': {'charset':'utf8mb4'}
	    }
	}
}

DATABASES = DATABASE_LIST[ENV]

