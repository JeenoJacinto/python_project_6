import time

from django.core.urlresolvers import reverse # lets us reverse a url name cont-
# gets the name of a url and uses that to get the route and view it goes to
from django.test import TestCase
from django.utils import timezone

from .models import Mineral, DescriptionCount
# Create your tests here.

# activating test: python manage.py test
class MineralModelTests(TestCase):
    def test_mineral_creation(self):
        item = {
    		"name": "Abelsonite",
    		"image filename": "240px-Abelsonite_-_Green" +
            "_River_Formation%2C_Uintah_County%2C_Utah%2C_USA.jpg",
    		"image caption": "Abelsonite from the" +
            " Green River Formation, Uintah County, Utah, US",
    		"category": "Organic",
    		"formula": "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
    		"strunz classification": "10.CA.20",
    		"crystal system": "Triclinic",
    		"unit cell": "a = 8.508 Å, b = 11.185 Åc=7.299" +
            " Å, α = 90.85°β = 114.1°, γ = 79.99°Z = 1",
    		"color": "Pink-purple, dark greyish" +
            " purple, pale purplish red, reddish brown",
    		"crystal symmetry": "Space group: P1 or P1Point group: 1 or 1",
    		"cleavage": "Probable on {111}",
    		"mohs scale hardness": "2–3",
    		"luster": "Adamantine, sub-metallic",
    		"streak": "Pink",
    		"diaphaneity": "Semitransparent",
    		"optical properties": "Biaxial",
    		"group": "Organic Minerals"
    	}
        formatted_kwargs = {}
        for field in item:
            formatted_kwargs[field.replace(' ', '_')] = item[field]
            # replaces spaces with underscore to fit model fields
        obj = Mineral(**formatted_kwargs)
        obj.save()
        mineral = Mineral.objects.get()
        time.sleep(.002)
        now = timezone.now()
        self.assertLess(mineral.created_at, now)
    # tests that course was created before now was defined

class DescriptionCountModelTest(TestCase):
    def test_description_count_creation(self):
        description_count_model = DescriptionCount.objects.create(
            name=230,
            image_filename=230,
            image_caption=230,
            category=214,
            formula=119,
            strunz_classification=150,
            color=192,
            crystal_system=173,
            unit_cell=210,
            crystal_symmetry=219,
            cleavage=154,
            mohs_scale_hardness=118,
            luster=201,
            streak=207,
            diaphaneity=140,
            optical_properties=139,
            refractive_index=145,
            crystal_habit=204,
            specific_gravity=102,
            group=90,
        )
        self.assertEqual(description_count_model.name, 230)


class MineralViewsTests(TestCase):
    def setUp(self):
        item = {
    		"name": "Abelsonite",
    		"image filename": "240px-Abelsonite_-_Green_River_Formation" +
            "%2C_Uintah_County%2C_Utah%2C_USA.jpg",
    		"image caption": "Abelsonite from the Green River" +
            " Formation, Uintah County, Utah, US",
    		"category": "Organic",
    		"formula": "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
    		"strunz classification": "10.CA.20",
    		"crystal system": "Triclinic",
    		"unit cell": "a = 8.508 Å, b = 11.185" +
            " Åc=7.299 Å, α = 90.85°β = 114.1°, γ = 79.99°Z = 1",
    		"color": "Pink-purple, dark greyish " +
            "purple, pale purplish red, reddish brown",
    		"crystal symmetry": "Space group: P1 or P1Point group: 1 or 1",
    		"cleavage": "Probable on {111}",
    		"mohs scale hardness": "2–3",
    		"luster": "Adamantine, sub-metallic",
    		"streak": "Pink",
    		"diaphaneity": "Semitransparent",
    		"optical properties": "Biaxial",
    		"group": "Organic Minerals"
    	}
        formatted_kwargs = {}
        for field in item:
            formatted_kwargs[field.replace(' ', '_')] = item[field]
            # replaces spaces with underscore to fit model fields
        obj = Mineral(**formatted_kwargs)
        obj.save()
        item = {
    		"name": "Abernathyite",
    		"image filename": "240px-Abernathyite%2C_Heinrichite-497484.jpg",
    		"image caption": "Pale yellow abernathyite crystals " +
            "and green heinrichite crystals",
    		"category": "Arsenate",
    		"formula": "K(UO<sub>2</sub>)(AsO<sub>4</sub>)·<sub>" +
            "3</sub>H<sub>2</sub>O",
    		"strunz classification": "08.EB.15",
    		"crystal system": "Tetragonal",
    		"unit cell": "a = 7.176Å, c = 18.126ÅZ = 4",
    		"color": "Yellow",
    		"crystal symmetry": "H-M group: 4/m 2/m 2/mSpace group: P4/ncc",
    		"cleavage": "Perfect on {001}",
    		"mohs scale hardness": "2.5–3",
    		"luster": "Sub-Vitreous, resinous, waxy, greasy",
    		"streak": "Pale yellow",
    		"diaphaneity": "Transparent",
    		"optical properties": "Uniaxial (-)",
    		"refractive index": "nω = 1.597 – 1.608nε = 1.570",
    		"group": "Arsenates"
    	}
        formatted_kwargs = {}
        for field in item:
            formatted_kwargs[field.replace(' ', '_')] = item[field]
            # replaces spaces with underscore to fit model fields
        obj = Mineral(**formatted_kwargs)
        obj.save()
        all_minerals = Mineral.objects.all()
        self.mineral = all_minerals[0]
        self.mineral2 = all_minerals[1]
        self.description_count = DescriptionCount.objects.create(
            name=230,
            image_filename=230,
            image_caption=230,
            category=214,
            formula=119,
            strunz_classification=150,
            color=192,
            crystal_system=173,
            unit_cell=210,
            crystal_symmetry=219,
            cleavage=154,
            mohs_scale_hardness=118,
            luster=201,
            streak=207,
            diaphaneity=140,
            optical_properties=139,
            refractive_index=145,
            crystal_habit=204,
            specific_gravity=102,
            group=90,
        )

    def test_mineral_list_view(self):
        """
        self.client is like a web browser it lets you make web requests to a
        url and it gives us back the status code and the html that come from
        that url. If it goes to a view in our django app we get additonal info
        """
        resp = self.client.get(reverse('mineral_data:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'mineral_data/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(
            reverse('mineral_data:detail', kwargs={'pk':self.mineral.pk})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'mineral_data/mineral_detail.html')
        self.assertContains(resp, self.mineral.name)
