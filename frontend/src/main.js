import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import PrimeVue from "primevue/config";

// Imprting UI Componets
import Button from "primevue/button";
import MultiSelect from "primevue/multiselect";
import ProgressSpinner from "primevue/progressspinner";
import InputText from "primevue/inputtext";
import ProgressBar from "primevue/progressbar";
import FileUpload from "primevue/fileupload";
import Listbox from "primevue/listbox";
import Divider from "primevue/divider";
import Menubar from "primevue/menubar";
import Card from "primevue/card";
import Steps from "primevue/steps";
import Menu from "primevue/menu";
import TabView from "primevue/tabview";
import TabPanel from "primevue/tabpanel";
import Panel from "primevue/panel";
import RadioButton from "primevue/radiobutton";
import SelectButton from "primevue/selectbutton";
import ScrollPanel from "primevue/scrollpanel";
import Dropdown from "primevue/dropdown";
import Slider from "primevue/slider";
import InputNumber from "primevue/inputnumber";
import Dialog from "primevue/dialog";
import Checkbox from "primevue/checkbox";
import TabMenu from "primevue/tabmenu";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import Chart from "primevue/chart";

import "primevue/resources/themes/arya-green/theme.css"; //theme
import "primevue/resources/primevue.min.css"; //core css
import "primeflex/primeflex.css";

import "primeicons/primeicons.css"; //icons

const app = createApp(App);

app.use(PrimeVue);
app.use(PrimeVue, { ripple: true });
app.component("Button", Button);
app.component("MultiSelect", MultiSelect);
app.component("ProgressSpinner", ProgressSpinner);
app.component("InputText", InputText);
app.component("ProgressBar", ProgressBar);
app.component("FileUpload", FileUpload);
app.component("Listbox", Listbox);
app.component("Divider", Divider);
app.component("Menubar", Menubar);
app.component("Card", Card);
app.component("Steps", Steps);
app.component("Menu", Menu);
app.component("TabView", TabView);
app.component("TabPanel", TabPanel);
app.component("Panel", Panel);
app.component("RadioButton", RadioButton);
app.component("SelectButton", SelectButton);
app.component("ScrollPanel", ScrollPanel);
app.component("Dropdown", Dropdown);
app.component("Slider", Slider);
app.component("InputNumber", InputNumber);
app.component("Dialog", Dialog);
app.component("Checkbox", Checkbox);
app.component("TabMenu", TabMenu);
app.component("DataTable", DataTable);
app.component("Column", Column);
app.component("Chart", Chart);

app.use(router).mount("#app");

