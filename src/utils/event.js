class Event {
    constructor() {
        this.events = {};
    }

     on(eventName, fn) {
        this.events[eventName] = this.events[eventName] || [];
        this.events[eventName].push(fn);
    }
    emit = (eventName, data) => (this.events[eventName]) ? this.events[eventName].forEach(fn => fn(data)) : '';
}

export default new Event();