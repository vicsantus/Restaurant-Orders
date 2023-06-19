from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Mock
    ingres1 = Ingredient("presunto")
    ingres2 = Ingredient("ovo")

    # Teste funcional
    assert ingres1 == Ingredient("presunto")
    assert ingres2 != Ingredient("presunto")

    # Teste eq
    assert (ingres1 == ingres2) is False
    assert (ingres1 == Ingredient("presunto")) is True

    # Teste hash
    assert {ingres1, ingres2} == {Ingredient("presunto"), Ingredient("ovo")}
    assert hash(ingres1) == hash(Ingredient("presunto"))
    assert hash(ingres2) != hash(Ingredient("presunto"))

    # Teste restrictions
    assert ingres1.restrictions == Ingredient("presunto").restrictions
    assert ingres2.restrictions != Ingredient("presunto").restrictions

    # Teste repr
    assert repr(ingres1) == "Ingredient('presunto')"
    assert repr(ingres2) != "Ingredient('presunto')"

    # Teste name
    assert ingres1.name == "presunto"
