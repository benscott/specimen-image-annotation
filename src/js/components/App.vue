<template>
    <div id="app">
        <div id="loading" v-if="loading">
            <icon name="spinner" scale="2" class="fa-spin"></icon>
        </div>
        <div class="col-sm-9">
            <image-viewer :url="url" v-on:imageLoaded="onImageLoaded"></image-viewer>
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
    import ImageViewer from './ImageViewer.vue';
    import Multiselect from 'vue-multiselect';

    export default {
        name: 'app',
        components: {
            "transcription-form": VueFormGenerator.component,
            ImageViewer
        },
        mounted: function () {
          console.log('mounted');
          this.loadSpecimen();
        },
        methods: {
            loadSpecimen: function() {
                this.loading = true;
                this.$http.get(this.$config.api).then(response => {
                        console.log("Record loaded");
                        this.url = '/src/assets/slides/' + response.body.record.file_name;
                        this.barcode = response.body.record.barcode;
                        this._id = response.body.record._id;
                    }, response => {
                      console.log('Fetch Failed');
                });
            },
            saveSpecimen: function(model) {
                let data = {
                    day: model.day.toString(),
                    month: model.month.toString(),
                    year: model.year.toString(),
                    barcode: this.barcode,
                    url: this.url,
                };
                this.$http.put(this.$config.api + '/' + this._id + '/', data).then(response => {
                        model.day = '';
                        model.month = '';
                        model.year = '';
                        console.log('SAVED RECORD');
                        this.loadSpecimen();
                    }, response => {
                      console.log('Save Failed');
                });
            },
            onSubmit: function(model) {
                console.log('SAVE');
                this.saveSpecimen(model);
                console.log("LOAD");
            },
            onImageLoaded: function(){
              this.loading = false;
            },

            numericRange: function(start, count){
              return Array.apply(0, Array(count))
                .map(function (element, index) {
                  return index + start;
              });
            },

        },
        data () {

            var years = this.numericRange(1800, 217);
            years.unshift("Not Shown");

            var days = this.numericRange(1, 30);
            days.unshift("Not Shown");

            return {
                url: null,
                barcode: null,
                _id: null,
                loading: true,
                model: {
                    day: null,
                    month: null,
                    year: null
                },
                schema: {
                    fields: [
                        {
                            type: "vueMultiSelect",
                            label: "Day",
                            model: "day",
                            required: true,
                            validator: VueFormGenerator.validators.required,
                            values: days,
                            selectOptions: {
                                closeOnSelect: true,
                                searchable: true,
                                showLabels: false,
                                selectOnTab: true
                            },
                        },
                        {
                            type: "vueMultiSelect",
                            label: "Month",
                            model: "month",
                            required: true,
                            validator: VueFormGenerator.validators.required,
                            values: [
                                "Not Shown",
                                "i January",
                                "ii February",
                                "iii March",
                                "iv April",
                                "v May",
                                "vi June",
                                "vii July",
                                "viii August",
                                "ix September",
                                "x October",
                                "xi November",
                                "xii December",
                            ],
                            selectOptions: {
                                closeOnSelect: true,
                                searchable: true,
                                showLabels: false
                            },
                        },
                        {
                            type: "vueMultiSelect",
                            label: "Year",
                            model: "year",
                            required: true,
                            validator: VueFormGenerator.validators.required,
                            values: years,
                            selectOptions: {
                                closeOnSelect: true,
                                searchable: true,
                                showLabels: false
                            },
                        },
                        {
                            "type": "submit",
                            validateBeforeSubmit: true,
                            buttonText: "Submit",
                            onSubmit: this.onSubmit,
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

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style src="../../sass/app.scss" lang="scss"></style>
