<template>
  <Steps :model="items" />
  <router-view />
</template>
<script>
export default {
  name: "Steps",
  data() {
    return {
      items: [
        {
          label: "Personal",
          to: "/steps",
        },
        {
          label: "Seat",
          to: "/steps/seat",
        },
        {
          label: "Payment",
          to: "/steps/payment",
        },
        {
          label: "Confirmation",
          to: "/steps/confirmation",
        },
      ],
    };
  },
};
</script>
<style></style>
