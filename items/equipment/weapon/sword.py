import dataclasses
import enum

from items.equipment.weapon.weapon import TwoHandedWeapon


class TwoHandedSwords(enum.Enum):
    CORRODED_BLADE = TwoHandedWeapon(
        level=3,
        required_level=1,
        required_strength=11,
        required_dexterity=11,
        required_intelligence=0,
        damage_floor=8,
        damage_ceiling=16,
        attack_speed=145,
        range=13,
        critical=500,
        modifiers=[AttributeModifier(modifies=CharacterAttributes.ACCURACY, increases=40)]
    )
    LONGSWORD = TwoHandedWeapon(
        level=...,
        required_level=8,
        required_strength=20,
        required_dexterity=17,
        required_intelligence=0,
        damage_floor=11,
        damage_ceiling=26,
        attack_speed=140,
        range=13,
        critical=500,
        modifiers=[AttributeModifier(modifies=CharacterAttributes.ACCURACY, adds=60)]
    )
    BASTARD_SWORD = TwoHandedWeapon(
        level=...,
        required_level=12,
        required_strength=21,
        required_dexterity=30,
        required_intelligence=0,
        damage_floor=17,
        damage_ceiling=29,
        attack_speed=145,
        range=13,
        critical=500,
        modifiers=[AttributeModifier(modifies=CharacterAttributes.ACCURACY, increases=60)]
    )
    TWO_HANDED_SWORD = TwoHandedWeapon(
        level=...,
        required_level=17,
        required_strength=33,
        required_dexterity=33,
        required_intelligence=0,
        damage_floor=20,
        damage_ceiling=38,
        attack_speed=140,
        range=13,
        critical=500,
        modifiers=[AttributeModifier(modifies=CharacterAttributes.ACCURACY, adds=120)]
    )
    ETCHED_GREATSWORD = TwoHandedWeapon(
        level=...,
        required_level=22,
        required_strength=45,
        required_dexterity=38,
        required_intelligence=0,
        damage_floor=23,
        damage_ceiling=48,
        attack_speed=140,
        range=13,
        critical=500,
        modifiers=[AttributeModifier(modifies=CharacterAttributes.ACCURACY, increases=60)]
    )
    ORNATE_SWORD = TwoHandedWeapon(
        level=...,
        required_level=27,
        required_strength=45,
        required_dexterity=54,
        required_intelligence=0,
        damage_floor=30,
        damage_ceiling=50,
        attack_speed=140,
        range=13,
        critical=500,
        modifiers=[AttributeModifier(modifies=CharacterAttributes.ACCURACY, adds=185)]
    )
    REBUKING_BLADE = TwoHandedWeapon(
        level=30,
        required_level=30,
        required_strength=54,
        required_dexterity=54,
        required_intelligence=0,
        damage_floor=34,
        damage_ceiling=63,
        attack_speed=130,
        range=13,
        critical=600,
        modifiers=[
            EventModifier(
                modifies=Events.CRITICAL,
                attribute=AttributeModifier(
                    modifies=CharacterAttributes.PENETRATION,
                    group=ELEMENTAL,
                    adds=100
                )
            )
        ]
    )
    SPECTRAL_SWORD = TwoHandedWeapon(
        level=32,
        required_level=32,
        required_strength=57,
        required_dexterity=57,
        required_intelligence=0,
        damage_floor=31,
        damage_ceiling=65,
        attack_speed=135,
        range=13,
        critical=500,
        modifiers=[AttributeModifier(modifies=CharacterAttributes.ACCURACY, increases=45)]
    )
    CURVED_BLADE = TwoHandedWeapon(
        level=35,
        required_level=35,
        required_strength=62,
        required_dexterity=73,
        required_intelligence=0,
        damage_floor=41,
        damage_ceiling=68,
        attack_speed=135,
        range=13,
        critical=600,
        modifiers=[AttributeModifier(modifies=CharacterAttributes.CRITICAL, adds=40)]
    )
    BUTCHER_SWORD = TwoHandedWeapon(
        level=36,
        required_level=36,
        required_strength=69,
        required_dexterity=58,
        required_intelligence=0,
        damage_floor=34,
        damage_ceiling=79,
        attack_speed=130,
        range=13,
        critical=500,
        modifiers=[AttributeModifier(modifies=CharacterAttributes.ACCURACY, adds=250)]
    )