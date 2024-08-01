from pathlib import Path

import attr
import lingpy
from clldutils.misc import slug
import pylexibank


@attr.s
class CustomLanguage(pylexibank.Language):
    Village = attr.ib(default=None)
    Source = attr.ib(default=None)
    Family = attr.ib(default=None)
    SubGroup = attr.ib(default=None)
    DialectGroup = attr.ib(default=None)
    Phylum = attr.ib(default=None)


class Dataset(pylexibank.Dataset):
    dir = Path(__file__).parent
    id = "hantganbangime"
    language_class = CustomLanguage
    writer_options = dict(keep_languages=False, keep_parameters=False)

    def cmd_makecldf(self, args):
        wl = lingpy.Wordlist(str(self.raw_dir / "D_subset-300-22.tsv"))
        args.writer.add_sources()
        args.writer.add_languages(id_factory="Name")
        source_lookup = {language["ID"]: language["Source"] for language in self.languages}
        concepts = {}
        for concept in self.conceptlists[0].concepts.values():
            idx = concept.number + "_" + slug(concept.english)
            args.writer.add_concept(
                ID=idx,
                Name=concept.english,
                Concepticon_ID=concept.concepticon_id,
                Concepticon_Gloss=concept.concepticon_gloss,
            )
            concepts[concept.english] = idx
        for k in pylexibank.progressbar(wl, desc="wl-to-cldf", total=len(wl)):
            if wl[k, "tokens"]:
                args.writer.add_form(
                    Language_ID=wl[k, "doculect"],
                    Parameter_ID=concepts[wl[k, "concept"]],
                    Value=wl[k, "ipa"].strip() or "".join(wl[k, "tokens"]),
                    Form=wl[k, "ipa"].strip().replace(" ", "_") or "".join(wl[k, "tokens"]),
                    Source=[source_lookup[wl[k, "doculect"]]],
                    Comment=wl[k, "note"],
                )
