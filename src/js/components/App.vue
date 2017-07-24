<template>
    <div id="app">
        <div class="col-sm-9">
            <div id="loading" v-if="loading">
                <icon name="floppy-o" scale="8"></icon>
            </div>
            <image-viewer :url="url" v-else></image-viewer>
         </div>
        <div class="col-sm-3">
            <h1>{{ barcode }}</h1>
            <form v-on:submit.prevent>
                <transcription-form :schema="schema" :model="model" :options="formOptions"></transcription-form>
            </form>
        </div>
    </div>
</template>

<script>

    import VueFormGenerator from "vue-form-generator";
    import ImageViewer from './ImageViewer.vue'

    export default {
        name: 'app',
        components: {
            "transcription-form": VueFormGenerator.component,
            ImageViewer
        },
        mounted: function () {
          this.loadSpecimen();
        },
        methods: {
            loadSpecimen: function() {
                this.$http.get(this.$config.api + '/not-transcribed').then(response => {
                        console.log("Record loaded");
                        this.url = response.body.record.url;
                        this.barcode = response.body.record.barcode;
                        this._id = response.body.record._id;
                        this.loading = false;
                    }, response => {
                      console.log('Fetch Failed');
                });
            },
            saveSpecimen: function(country) {
                let data = {
                    country: country.toString(),
                    barcode: this.barcode,
                    url: this.url,
                };
                this.loading = true;
                this.$http.put(this.$config.api + '/' + this._id + '/', data).then(response => {
                        console.log('SAVED RECORD');
                        this.loadSpecimen();
                    }, response => {
                      console.log('Save Failed');
                });
            },
            onSubmit: function(model) {
                this.saveSpecimen(model.country);
                console.log("LOAD");
            }
        },
        data () {
            return {
                loading: true,
                url: null,
                barcode: null,
                _id: null,
                model: {
                    country: null
                },
                schema: {
                    fields: [
                        {
                            type: "select",
                            label: "Country",
                            model: "country",
                            required: true,
                            validator: VueFormGenerator.validators.required,
                            values: [
                                {id: "none", name: "No Country Stated"},
                                {id: "other", name: "Other"},
                                {id: 138002, name: "Afghanistan"},
                                {id: 601746, name: "Akrotiri and Dhekelia"},
                                {id: 796407, name: "Åland"},
                                {id: 139385, name: "Albania"},
                                {id: 137027, name: "Algeria"},
                                {id: 139143, name: "American Samoa"},
                                {id: 139386, name: "Andorra"},
                                {id: 137046, name: "Angola"},
                                {id: 140824, name: "Anguilla"},
                                {id: 137960, name: "Antarctica"},
                                {id: 140825, name: "Antigua and Barbuda"},
                                {id: 141198, name: "Argentina"},
                                {id: 138014, name: "Armenia"},
                                {id: 140826, name: "Aruba"},
                                {id: 139152, name: "Australia"},
                                {id: 139396, name: "Austria"},
                                {id: 138091, name: "Azerbaijan"},
                                {id: 140848, name: "Bahamas"},
                                {id: 138109, name: "Bahrain"},
                                {id: 138176, name: "Bangladesh"},
                                {id: 140849, name: "Barbados"},
                                {id: 139403, name: "Belarus"},
                                {id: 139418, name: "Belgium"},
                                {id: 140856, name: "Belize"},
                                {id: 137059, name: "Benin"},
                                {id: 140857, name: "Bermuda"},
                                {id: 138201, name: "Bhutan"},
                                {id: 141207, name: "Bolivia"},
                                {id: 601744, name: "Bonaire, Sint Eustatius and Saba"},
                                {id: 139421, name: "Bosnia and herzegovina"},
                                {id: 137069, name: "Botswana"},
                                {id: 137961, name: "Bouvet island"},
                                {id: 141235, name: "Brazil"},
                                {id: 138202, name: "British Indian Ocean Territory"},
                                {id: 141167, name: "Virgin Islands, British"},
                                {id: 138207, name: "Brunei Darussalam"},
                                {id: 139451, name: "Bulgaria"},
                                {id: 137115, name: "Burkina Faso"},
                                {id: 137132, name: "Burundi"},
                                {id: 138232, name: "Cambodia"},
                                {id: 137143, name: "Cameroon"},
                                {id: 140871, name: "Canada"},
                                {id: 137185, name: "Cape verde"},
                                {id: 140872, name: "Cayman Islands"},
                                {id: 137203, name: "Central African Republic"},
                                {id: 137218, name: "Chad"},
                                {id: 141249, name: "Chile"},
                                {id: 138268, name: "China"},
                                {id: 138269, name: "Christmas island"},
                                {id: 4502627, name: "Clipperton Island"},
                                {id: 138270, name: "Cocos (keeling) islands"},
                                {id: 141283, name: "Colombia"},
                                {id: 137222, name: "Comoros"},
                                {id: 139153, name: "Cook Islands"},
                                {id: 140880, name: "Costa Rica"},
                                {id: 137263, name: "Côte d'Ivoire"},
                                {id: 139473, name: "Croatia"},
                                {id: 140897, name: "Cuba"},
                                {id: 4725113, name: "Curaçao"},
                                {id: 138277, name: "Cyprus"},
                                {id: 139488, name: "Czech Republic"},
                                {id: 137246, name: "Congo, the Democratic Republic of the"},
                                {id: 139505, name: "Denmark"},
                                {id: 137270, name: "Djibouti"},
                                {id: 140898, name: "Dominica"},
                                {id: 140929, name: "Dominican Republic"},
                                {id: 141306, name: "Ecuador"},
                                {id: 137297, name: "Egypt"},
                                {id: 140944, name: "El Salvador"},
                                {id: 137306, name: "Equatorial Guinea"},
                                {id: 137314, name: "Eritrea"},
                                {id: 139521, name: "Estonia"},
                                {id: 137326, name: "Ethiopia"},
                                {id: 141307, name: "Falkland islands (malvinas)"},
                                {id: 139522, name: "Faroe Islands"},
                                {id: 139173, name: "Fiji"},
                                {id: 139529, name: "Finland"},
                                {id: 139632, name: "France"},
                                {id: 141308, name: "French Guiana"},
                                {id: 139174, name: "French Polynesia"},
                                {id: 137962, name: "French Southern Territories"},
                                {id: 137336, name: "Gabon"},
                                {id: 137343, name: "Gambia"},
                                {id: 138290, name: "Georgia"},
                                {id: 139649, name: "Germany"},
                                {id: 137354, name: "Ghana"},
                                {id: 139650, name: "Gibraltar"},
                                {id: 139718, name: "Greece"},
                                {id: 140945, name: "Greenland"},
                                {id: 140946, name: "Grenada"},
                                {id: 140947, name: "Guadeloupe"},
                                {id: 139135, name: "Guam"},
                                {id: 140970, name: "Guatemala"},
                                {id: 552558, name: "Guernsey"},
                                {id: 137395, name: "Guinea"},
                                {id: 137405, name: "Guinea-Bissau"},
                                {id: 141319, name: "Guyana"},
                                {id: 140980, name: "Haiti"},
                                {id: 137963, name: "Heard island and mcdonald islands"},
                                {id: 140999, name: "Honduras"},
                                {id: 138291, name: "Hong Kong"},
                                {id: 139762, name: "Hungary"},
                                {id: 139769, name: "Iceland"},
                                {id: 138327, name: "India"},
                                {id: 138360, name: "Indonesia"},
                                {id: 138389, name: "Iran, Islamic Republic of"},
                                {id: 138408, name: "Iraq"},
                                {id: 139799, name: "Ireland"},
                                {id: 581857, name: "Isle of Man"},
                                {id: 138415, name: "Israel"},
                                {id: 139904, name: "Italy"},
                                {id: 141016, name: "Jamaica"},
                                {id: 138465, name: "Japan"},
                                {id: 552577, name: "Jersey"},
                                {id: 138484, name: "Jordan"},
                                {id: 138502, name: "Kazakhstan"},
                                {id: 137414, name: "Kenya"},
                                {id: 139198, name: "Kiribati"},
                                {id: 601747, name: "Kosovo"},
                                {id: 138540, name: "Kuwait"},
                                {id: 138549, name: "Kyrgyzstan"},
                                {id: 138568, name: "Lao People's Democratic Republic"},
                                {id: 139957, name: "Latvia"},
                                {id: 138575, name: "Lebanon"},
                                {id: 137425, name: "Lesotho"},
                                {id: 137441, name: "Liberia"},
                                {id: 137476, name: "Libyan Arab Jamahiriya"},
                                {id: 139969, name: "Liechtenstein"},
                                {id: 139980, name: "Lithuania"},
                                {id: 139996, name: "Luxembourg"},
                                {id: 138576, name: "Macao"},
                                {id: 139997, name: "Macedonia, the former Yugoslav Republic of"},
                                {id: 137483, name: "Madagascar"},
                                {id: 137511, name: "Malawi"},
                                {id: 138593, name: "Malaysia"},
                                {id: 138614, name: "Maldives"},
                                {id: 137521, name: "Mali"},
                                {id: 139998, name: "Malta"},
                                {id: 139231, name: "Marshall Islands"},
                                {id: 141018, name: "Martinique"},
                                {id: 137535, name: "Mauritania"},
                                {id: 137553, name: "Mauritius"},
                                {id: 137554, name: "Mayotte"},
                                {id: 141051, name: "Mexico"},
                                {id: 139236, name: "Micronesia, Federated States of"},
                                {id: 140012, name: "Moldova, Republic of"},
                                {id: 140013, name: "Monaco"},
                                {id: 138637, name: "Mongolia"},
                                {id: 417337, name: "Montenegro"},
                                {id: 141052, name: "Montserrat"},
                                {id: 137625, name: "Morocco"},
                                {id: 137637, name: "Mozambique"},
                                {id: 138652, name: "Myanmar"},
                                {id: 137651, name: "Namibia"},
                                {id: 139237, name: "Nauru"},
                                {id: 138667, name: "Nepal"},
                                {id: 140026, name: "Netherlands"},
                                {id: 139238, name: "New Caledonia"},
                                {id: 139255, name: "New Zealand"},
                                {id: 141071, name: "Nicaragua"},
                                {id: 137660, name: "Niger"},
                                {id: 137698, name: "Nigeria"},
                                {id: 139256, name: "Niue"},
                                {id: 139257, name: "Norfolk Island"},
                                {id: 138516, name: "Korea, Democratic People's Republic of"},
                                {id: 601748, name: "Northern Cyprus"},
                                {id: 139258, name: "Northern Mariana Islands"},
                                {id: 140048, name: "Norway"},
                                {id: 138677, name: "Oman"},
                                {id: 138686, name: "Pakistan"},
                                {id: 139259, name: "Palau"},
                                {id: 141085, name: "Panama"},
                                {id: 139280, name: "Papua New Guinea"},
                                {id: 330290, name: "Paracel Islands"},
                                {id: 141338, name: "Paraguay"},
                                {id: 141364, name: "Peru"},
                                {id: 138768, name: "Philippines"},
                                {id: 139281, name: "Pitcairn"},
                                {id: 140065, name: "Poland"},
                                {id: 140086, name: "Portugal"},
                                {id: 141086, name: "Puerto Rico"},
                                {id: 138778, name: "Qatar"},
                                {id: 137223, name: "Congo"},
                                {id: 137717, name: "Réunion"},
                                {id: 140129, name: "Romania"},
                                {id: 140219, name: "Russian Federation"},
                                {id: 137716, name: "Rwanda"},
                                {id: 137718, name: "Saint Helena"},
                                {id: 141087, name: "Saint Kitts and Nevis"},
                                {id: 141088, name: "Saint Lucia"},
                                {id: 141089, name: "Saint Pierre and Miquelon"},
                                {id: 141090, name: "Saint Vincent and the Grenadines"},
                                {id: 313302, name: "Saint-Barthélemy"},
                                {id: 601749, name: "Saint-Martin"},
                                {id: 139293, name: "Samoa"},
                                {id: 140220, name: "San Marino"},
                                {id: 137721, name: "Sao Tome and Principe"},
                                {id: 138792, name: "Saudi Arabia"},
                                {id: 137733, name: "Senegal"},
                                {id: 112352, name: "Serbia"},
                                {id: 137734, name: "Seychelles"},
                                {id: 137739, name: "Sierra Leone"},
                                {id: 138793, name: "Singapore"},
                                {id: 582536, name: "Sint Maarten"},
                                {id: 140234, name: "Slovakia"},
                                {id: 140428, name: "Slovenia"},
                                {id: 139302, name: "Solomon Islands"},
                                {id: 137758, name: "Somalia"},
                                {id: 137768, name: "South Africa"},
                                {id: 137966, name: "South Georgia and the South Sandwich Islands"},
                                {id: 138533, name: "Korea, Republic of"},
                                {id: 468060, name: "South Sudan"},
                                {id: 140481, name: "Spain"},
                                {id: 601750, name: "Spratly islands"},
                                {id: 138819, name: "Sri Lanka"},
                                {id: 137795, name: "Sudan"},
                                {id: 141375, name: "Suriname"},
                                {id: 140482, name: "Svalbard and jan mayen"},
                                {id: 137800, name: "Swaziland"},
                                {id: 140504, name: "Sweden"},
                                {id: 140531, name: "Switzerland"},
                                {id: 138834, name: "Syrian Arab Republic"},
                                {id: 138858, name: "Taiwan, Province of China"},
                                {id: 138863, name: "Tajikistan"},
                                {id: 137827, name: "Tanzania, United Republic of"},
                                {id: 138941, name: "Thailand"},
                                {id: 138942, name: "Timor-Leste"},
                                {id: 137833, name: "Togo"},
                                {id: 139316, name: "Tokelau"},
                                {id: 139317, name: "Tonga"},
                                {id: 141107, name: "Trinidad and Tobago"},
                                {id: 137858, name: "Tunisia"},
                                {id: 139025, name: "Turkey"},
                                {id: 139032, name: "Turkmenistan"},
                                {id: 141108, name: "Turks and Caicos Islands"},
                                {id: 139318, name: "Tuvalu"},
                                {id: 137937, name: "Uganda"},
                                {id: 140559, name: "Ukraine"},
                                {id: 139040, name: "United Arab Emirates"},
                                {id: 141424, name: "United Kingdom"},
                                {id: 141166, name: "United States of America"},
                                {id: 139328, name: "United states minor outlying islands"},
                                {id: 141395, name: "Uruguay"},
                                {id: 139055, name: "Uzbekistan"},
                                {id: 139335, name: "Vanuatu"},
                                {id: 139719, name: "Holy See (Vatican City State)"},
                                {id: 141421, name: "Venezuela"},
                                {id: 139056, name: "Vietnam"},
                                {id: 141168, name: "Virgin islands, u.s."},
                                {id: 139336, name: "Wallis and futuna"},
                                {id: 137938, name: "Western Sahara"},
                                {id: 139142, name: "Yemen"},
                                {id: 137948, name: "Zambia"},
                                {id: 137959, name: "Zimbabwe"}
                            ]
                        },
                        {
                            "type": "submit",
                            validateBeforeSubmit: true,
                            buttonText: "Submit",
                            onSubmit:this.onSubmit,
                        }
                    ]
                },
                formOptions: {
                    validateAfterChanged: true,
                }
            }

        }
    }
</script>

<style src="../../sass/app.scss" lang="scss"></style>
