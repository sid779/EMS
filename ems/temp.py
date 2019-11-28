html_message = render_to_string('ems/mail_host.html', {'data':obj})
			plain_message = strip_tags(html_message)
			from_email = "sskuuo@gmail.com"
			to_email = "xayipam293@tmail1.com"
			send_mail(
			'Visitor details',
			plain_message,
			from_email,
			[to_email],
			fail_silently=False,
			html_message = html_message,
			)




html_message = render_to_string('ems/mail_visitor.html', {'data':cur_data})
			plain_message = strip_tags(html_message)
			from_email = settings.EMAIL_HOST_USER
			to_email = cur_data.email
			send_mail(
			'Your visiting details',
			plain_message,
			from_email,
			[to_email],
			fail_silently=False,
			html_message = html_message,
			)	
