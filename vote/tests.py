from vote.models import Profile
from django.test import TestCase

# Create your tests here.
class ProfileTestClass(TestCase):
  def setUp(self):
    self.profile = Profile(
      photo = 'test.jpeg',
      name = 'Test Name',
      userName = 'testUser',
      contact = 'test@user.com',
      bio = 'This is a bio of a test user who is running texts to make sure the models are working properly.'
    )
    self.profile.save()
    
  def testInstance(self):
    self.assertTrue(self.profile, Profile)
    
  def testSave(self):
    self.profile.saveProfile()
    profile = Profile.objects.all()
    self.assertTrue(len(profile) > 0)