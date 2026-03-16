for class in death-knight demon-hunter druid evoker hunter mage monk paladin priest rogue shaman warlock warrior; do
  for spec in $(ls "$class"); do
    
    # Determine role for URL suffix
    case "$spec" in
      blood|vengeance|guardian|brewmaster|protection) role="tank" ;;
      *) role="dps" ;;
    esac

    # Map Hero Talents based on your reference
    case "$class/$spec" in
      "death-knight/blood") ht1="deathbringer"; ht2="sanlayn" ;;
      "death-knight/frost") ht1="deathbringer"; ht2="rider-of-the-apocalypse" ;;
      "death-knight/unholy") ht1="rider-of-the-apocalypse"; ht2="sanlayn" ;;
      
      "demon-hunter/havoc") ht1="aldrachi-reaver"; ht2="fel-scarred" ;;
      "demon-hunter/devourer") ht1="annihilator"; ht2="void-scarred" ;;
      "demon-hunter/vengeance") ht1="aldrachi-reaver"; ht2="annihilator" ;;
      
      "druid/balance") ht1="elunes-chosen"; ht2="keeper-of-the-grove" ;;
      "druid/feral") ht1="druid-of-the-claw"; ht2="wildstalker" ;;
      "druid/guardian") ht1="druid-of-the-claw"; ht2="elunes-chosen" ;;
      
      "evoker/devastation") ht1="flameshaper"; ht2="scalecommander" ;;
      "evoker/augmentation") ht1="chronowarden"; ht2="scalecommander" ;;
      
      "hunter/beast-mastery") ht1="dark-ranger"; ht2="pack-leader" ;;
      "hunter/marksmanship") ht1="dark-ranger"; ht2="sentinel" ;;
      "hunter/survival") ht1="pack-leader"; ht2="sentinel" ;;
      
      "mage/arcane") ht1="spellslinger"; ht2="sunfury" ;;
      "mage/fire") ht1="frostfire"; ht2="sunfury" ;;
      "mage/frost") ht1="frostfire"; ht2="spellslinger" ;;
      
      "monk/brewmaster") ht1="master-of-harmony"; ht2="shado-pan" ;;
      "monk/windwalker") ht1="conduit-of-the-celestials"; ht2="shado-pan" ;;
      
      "paladin/protection") ht1="lightsmith"; ht2="templar" ;;
      "paladin/retribution") ht1="herald-of-the-sun"; ht2="templar" ;;
      
      "priest/shadow") ht1="archon"; ht2="voidweaver" ;;
      
      "rogue/assassination") ht1="deathstalker"; ht2="fatebound" ;;
      "rogue/outlaw") ht1="fatebound"; ht2="trickster" ;;
      "rogue/subtlety") ht1="deathstalker"; ht2="trickster" ;;
      
      "shaman/elemental") ht1="farseer"; ht2="stormbringer" ;;
      "shaman/enhancement") ht1="stormbringer"; ht2="totemic" ;;
      
      "warlock/affliction") ht1="hellcaller"; ht2="soul-harvester" ;;
      "warlock/demonology") ht1="diabolist"; ht2="soul-harvester" ;;
      "warlock/destruction") ht1="diabolist"; ht2="hellcaller" ;;
      
      "warrior/arms") ht1="colossus"; ht2="slayer" ;;
      "warrior/fury") ht1="mountain-thane"; ht2="slayer" ;;
      "warrior/protection") ht1="colossus"; ht2="mountain-thane" ;;
      
      *) ht1="unknown"; ht2="unknown" ;;
    esac

    # Write the file
    cat <<EOF > "$class/$spec/info_links.md"
# $class - $spec Links

## Guides
https://www.wowhead.com/guide/classes/$class/$spec/overview-pve-$role
https://www.wowhead.com/guide/classes/$class/$spec/basics
https://www.wowhead.com/guide/classes/$class/$spec/abilities-talents-pve-$role
https://www.wowhead.com/guide/classes/$class/$spec/stat-priority-pve-$role
https://www.wowhead.com/guide/classes/$class/$spec/rotation-cooldowns-pve-$role
https://www.wowhead.com/guide/classes/$class/$spec/enchants-gems-pve-$role

## Talents use talent_extraction.md method to extract data
https://www.wowhead.com/talent-calc/$class/$spec/$ht1
https://www.wowhead.com/talent-calc/$class/$spec/$ht2
EOF
  done
done
