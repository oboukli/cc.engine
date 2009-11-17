from routes.route import Route

licenses_routes = [
    Route("licenses_index", "/",
          controller="cc.engine.licenses.views:licenses_view"),
    Route("license_deed",
          "/{code}/{version}/",
          controller="cc.engine.licenses.views:license_deed_view"),
    Route("license_deed_lang",
          "/{code}/{version}/deed.{target_lang}",
          controller="cc.engine.licenses.views:license_deed_view"),
    Route("license_rdf",
          "/{code}/{version}/rdf",
          controller="cc.engine.licenses.views:license_rdf_view"),
    Route("license_legalcode",
          "/{code}/{version}/legalcode",
          controller="cc.engine.licenses.views:license_legalcode_view"),
    Route("license_legalcode_plain",
          "/{code}/{version}/legalcode-plain",
          controller="cc.engine.licenses.views:license_legalcode_plain_view"),
    Route("license_deed_jurisdiction",
          "/{code}/{version}/{jurisdiction}/",
          controller="cc.engine.licenses.views:license_deed_view"),
    Route("license_deed_lang_jurisdiction",
          "/{code}/{version}/{jurisdiction}/deed.{target_lang}",
          controller="cc.engine.licenses.views:license_deed_view"),
    Route("license_rdf_jurisdiction",
          "/{code}/{version}/{jurisdiction}/rdf",
          controller="cc.engine.licenses.views:license_rdf_view"),
    Route("license_legalcode_jurisdiction",
          "/{code}/{version}/jurisdiction}/legalcode",
          controller="cc.engine.licenses.views:license_legalcode_view"),
    Route("license_legalcode_plain_jurisdiction",
          "/{code}/{version}/jurisdiction}/legalcode-plain",
          controller="cc.engine.licenses.views:license_legalcode_plain_view")]

cc0_routes = [
    Route("cc0_deed", "/{version}/",
          code='CC0', controller="cc.engine.licenses.views:license_deed_view"),
    Route("cc0_deed_lang", "/{version}/deed.{target_lang}",
          code='CC0', controller="cc.engine.licenses.views:license_deed_view"),
    Route("cc0_rdf", "/{version}/rdf",
          code='CC0', controller="cc.engine.licenses.views:license_rdf_view"),
    Route("cc0_legalcode", "/{version}/legalcode", code='CC0',
          controller="cc.engine.licenses.views:license_legalcode_view"),
    Route("cc0_legalcode_plain", "/{version}/legalcode-plain", code='CC0',
          controller="cc.engine.licenses.views:license_legalcode_plain_view")]
