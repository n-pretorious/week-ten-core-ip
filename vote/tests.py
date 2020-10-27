from vote.models import Profile, Project, Rate
from django.test import TestCase

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(
            photo="test.jpeg",
            name="Test Name",
            userName="testUser",
            contact="test@user.com",
            bio="This is a bio of a test user who is running texts to make sure the models are working properly.",
        )
        self.profile.save()

    def testInstance(self):
        self.assertTrue(self.profile, Profile)

    def saveProfileTest(self):
        self.profile.saveProfile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def getProfileByIdTest(self):
        profile = Profile.getProfileById(self.profile.pk)
        self.assertEqual(profile, self.profile)


class ProjectTestClass(TestCase):
    def setUp(self):
        self.project = Project(
            image="test.jpeg",
            title="New Project",
            description="This is a new project being tested.",
            link="www.newproject.com",
            # profile="",
        )
        self.project.save()

    def testInstance(self):
        self.assertTrue(self.project, Project)

    def saveProjectTest(self):
        self.project.saveProject()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)

    def getProjectByIdTest(self):
        project = Project.getProjectById(self.project.pk)
        self.assertEqual(project, self.project)


class RatingTestClass(TestCase):
    def setUp(self):
        self.rating = Rate(
            project=Project(
                image="test.jpeg",
                title="New Project",
                description="This is a new project being tested.",
                link="www.newproject.com",
                # profile="",
            ),
            design=3,
            usability=6,
            content=9,
            # author
        )

    def testInstance(self):
        self.assertTrue(self.rating, Rate)

    def saveRatingTest(self):
        self.rating.saveRating()
        ratings = Rate.objects.all()
        self.assertEqual(len(ratings) > 0)
