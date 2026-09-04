from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase

from .models import RegistroParada


class RegistroParadaModelTests(TestCase):
	def test_registro_parada_se_puede_crear_correctamente(self):
		hora = timezone.now()

		registro = RegistroParada.objects.create(
			id_carro='AGV-01',
			sensor='S-01',
			duracion=30,
			hora=hora,
		)

		self.assertIsNotNone(registro.pk)
		self.assertEqual(RegistroParada.objects.count(), 1)
		self.assertEqual(registro.id_carro, 'AGV-01')
		self.assertEqual(registro.sensor, 'S-01')
		self.assertEqual(registro.duracion, 30)
		self.assertEqual(registro.hora, hora)


class PaginasTests(TestCase):
	def setUp(self):
		self.usuario = get_user_model().objects.create_user(
			username='usuario_test',
			password='password-segura-123',
		)

	def test_dashboard_redirige_al_login_si_no_hay_sesion(self):
		respuesta = self.client.get(reverse('agv:dashboard'))

		self.assertRedirects(
			respuesta,
			f'{reverse("agv:login")}?next={reverse("agv:dashboard")}',
		)

	def test_paginas_cargan_correctamente_con_sesion_iniciada(self):
		self.client.force_login(self.usuario)

		for nombre_url in ('home', 'dashboard', 'historico'):
			with self.subTest(pagina=nombre_url):
				respuesta = self.client.get(reverse(f'agv:{nombre_url}'))

				self.assertEqual(respuesta.status_code, 200)
				self.assertTemplateUsed(respuesta, f'agv/{nombre_url}.html')
